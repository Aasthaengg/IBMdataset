import sys
tmp=sys.stdin.readline().rstrip()
def main():
   ans=0
   cnt=[0]*2019
   cnt[0]+=1
   t=0
   d=1
   for i in reversed(tmp):
      t=(t+int(i)*d)%2019
      cnt[t]+=1
      d=d*10%2019
   for i in cnt:
      ans+=i*(i-1)//2
   print(ans)
if __name__ == "__main__":
    main()