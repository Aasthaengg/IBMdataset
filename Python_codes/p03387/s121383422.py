ABC = list(map(int, input().split()))
ABC = sorted(ABC)[::-1]

diff1 = ABC[0]-ABC[1]
diff2 = ABC[1]-ABC[2]

cnt2 = 0

if diff2 % 2 ==0:
  cnt2 = diff2 /2
else:
  cnt2 = 2 + diff2 /2

ans = int(diff1 + cnt2)
print(ans)