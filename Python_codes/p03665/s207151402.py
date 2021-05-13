inp1, inp2 = map(int, input().split())
c = [int(i)&1 for i in input().split()]
add = sum(c)
if add:
    ans = 2**(inp1-1)
else:
    ans = 2**inp1*(1-inp2)
print(ans)