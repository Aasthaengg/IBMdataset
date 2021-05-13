n = int(input())
s = input()
w = s.count("W")
r = s.count("R")

left_w = 0
right_r = r
count = [left_w+right_r]
for i in range(0, n):
    if s[i] == "W":
        left_w += 1
    else:
        right_r -=1
    #print(s[:i], s[i:], s[i], left_w, right_r)
    count.append(max(left_w,right_r))
print(min(count))