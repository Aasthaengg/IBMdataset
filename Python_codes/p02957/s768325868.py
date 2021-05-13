#template
def inputlist(): return [int(k) for k in input().split()]
#template
A,B = inputlist()
if (A+B) % 2 == 0:
    print((A+B)//2)
else:
    print("IMPOSSIBLE")