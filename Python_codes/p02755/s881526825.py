import math
a,b=map(int,input().split())
ans=max(math.ceil(a/0.08),b*10)
au=math.ceil((a+1)/0.08)
bu=(b+1)*10
print(ans if ans < au and ans < bu else -1)