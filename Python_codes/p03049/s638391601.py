n = int(input())
s = [input() for _ in range(n)]
count = 0
a_count = 0
b_count = 0
ab_count = 0

for ss in s:
    count += ss.count("AB")
    if ss[0] == "B" and ss[-1] == "A":
        ab_count += 1
    elif ss[0] != "B" and ss[-1] == "A":
        a_count += 1
    elif ss[0] == "B" and ss[-1] != "A":
        b_count += 1

tmp_count = min(a_count,b_count)
if ab_count == 0:
    count += tmp_count
else:
    if a_count + b_count > 0:
        count += ab_count + tmp_count
    else:
        count += ab_count - 1
print(count)

