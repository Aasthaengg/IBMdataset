n=int(input())

a= list(map(int,input().split()))

a.sort()

plus_sum = a.pop(-1)
plus_memo = plus_sum
minas_sum = a.pop(0)
minas_memo = minas_sum

for aa in a:
    if 0 < aa:
        minas_sum -= aa
    else:
        plus_sum -= aa

print(plus_sum-minas_sum)

for aa in a:
    if 0 < aa:
        print(minas_memo, aa)
        minas_memo -= aa
    else:
        print(plus_memo, aa)
        plus_memo -= aa
print(plus_memo, minas_memo)