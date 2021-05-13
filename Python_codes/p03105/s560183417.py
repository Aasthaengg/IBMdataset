def main():
 a,b,c = map(int,input().split())
 cnt = 0
 ans = 0
 while cnt <= b:
     cnt += a
     if cnt <= b:
        ans += 1
     if ans == c:
         break
 print(ans)
main()