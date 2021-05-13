tmp = input().split(" ")
a_end = tmp[0][-1:]
b_start = tmp[1][:1]
b_end = tmp[1][-1:]
c_start = tmp[2][:1]

print("YES") if (a_end == b_start and b_end == c_start) else print("NO")