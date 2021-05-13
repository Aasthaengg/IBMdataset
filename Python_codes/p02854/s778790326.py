n = int(input())

stick = list(map(int, input().split()))

total = sum(stick)
mid = total // 2

cum = 0
midi = 0
for i, block in enumerate(stick):
    cum += block
    if cum >= mid:
        midi = i
        break

l1 = stick[:midi]
r1 = stick[midi:]
diff1 = abs(sum(l1) - sum(r1))
 
l2 = stick[:midi+1]
r2 = stick[midi+1:]
diff2 = abs(sum(l2) - sum(r2))
 
print(min(diff1, diff2))