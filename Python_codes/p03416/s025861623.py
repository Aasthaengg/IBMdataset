'''
リストや文字列の並び替え
↓↓↓
https://note.nkmk.me/python-reverse-reversed/
'''
a,b=map(int,(input().split()))
ans=0

for i in range(a,b+1):
  num=str(i)
  num_reverse=num[::-1]
  if num==num_reverse:
    ans+=1
print(ans)