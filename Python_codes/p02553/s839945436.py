def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
A,B,C,D=MI()
ans1=A*C
ans2=A*D
ans3=B*C
ans4=B*D
Max=max(ans1,ans2,ans3,ans4)
if A<=0<=B or C<=0<=D:
  Max=max(0,Max)
print(Max)