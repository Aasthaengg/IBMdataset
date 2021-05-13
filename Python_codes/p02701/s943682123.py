n=int(input())
dic={}
for i in range(n):
  s=input()
  dic[s]=1
print(len(list(dic.keys())))