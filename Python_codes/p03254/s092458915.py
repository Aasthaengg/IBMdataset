N, x = list(map(int, input().split()))
a = list(map(int, input().split()))
result = 0
sorted_a = sorted(a)
remain = x
for a_i in sorted_a:
    if remain >= a_i:
        result += 1
        remain -= a_i
    else:
        break

### 最後の子供にぴったりのお菓子をあげられなかった
if result == N and remain != 0:
    result -= 1
print(result)