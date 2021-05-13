input();a=1;d=eval('1'+'0'*18)
for i in input().split():a=min(a*int(i),d+1)
print([a,-1][a>d])