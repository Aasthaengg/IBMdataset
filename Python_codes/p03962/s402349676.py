def main():
 num = list(map(int,input().split()))
 ans = 1 ;
 if num[0]!=num[1]:
  ans+=1
 if num[0]!=num[2] and num[1]!=num[2]:
  ans+=1
 print(ans)
 
main()