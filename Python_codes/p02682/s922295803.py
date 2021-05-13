import sys
def main():
  a ,b ,c ,k = list(map(int,input().split()))
  if k > a:
    ans = a*1
    k-= a
  else:
    ans = (k)*1
    k = 0
#  print('a',k,ans)
  if k > b:
    k-= b
  else:
    k = 0
#  print('b',k,ans)
  if k > c and k>0:
    ans += (c)*-1
  else:
    ans += (k)*-1
    
  print(ans)   
#  print(k,ans)   
 
  
if __name__ == '__main__':
  main()
