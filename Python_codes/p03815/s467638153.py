x = int(input())

'''
if x <= 6:
    print(1)
'''
judge = x%11
#print(judge)
ans = 0
if judge == 0:
    ans = 2*(x//11)
elif judge > 6:
    ans = 2*(x//11)+2
else:
    ans = 2*(x//11)+1

print(ans)