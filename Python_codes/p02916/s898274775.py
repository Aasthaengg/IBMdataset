n = int(input())+1
inp1 = list(map(int, input().split()))
inp2 = list(map(int, input().split()))
inp3 = list(map(int, input().split()))
c, val = 0, 1
for i in range(n-1):
    c = (inp2[inp1[i] - val])+c
    if i > 0 and inp1[i] == inp1[i-val] + val:
        c = (inp3[inp1[i-val] - val])+c
print(c)
