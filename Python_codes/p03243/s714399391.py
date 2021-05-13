n = str(input())

ans_1 = 0
ans_2 = 0
x = int(n[0])
for i in range(len(n)):
    ans_1 += x * 10**i
    ans_2 += (x+1)*10**i
if ans_1 >= int(n):
    print(ans_1)
else:
    print(ans_2)