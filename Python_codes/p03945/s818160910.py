S = input()

prev = S[0]
switch_count = 0
for bw in S[1:]:
    if bw != prev:
        switch_count += 1
    prev = bw

print(switch_count)    