lines = input().split()
last_a = lines[0][len(lines[0])-1]
first_b = lines[1][0]
last_b = lines[1][len(lines[1])-1]
first_c = lines[2][0]

if last_a == first_b and last_b == first_c:
    print("YES")
else:
    print("NO")
