def main():
  num = list(map(int,input().split()))
  s=input()
  print(s[0:num[1]-1]+s[num[1]-1].lower()+s[num[1]:num[0]])
main()