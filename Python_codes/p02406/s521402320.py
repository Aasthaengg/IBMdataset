n = int(raw_input())
out_str = ""
for i in range(1,n+1):
    x = i
    if x % 3 == 0:
        out_str += " " + str(i)
        continue
    while x:
        if x % 10 == 3:
            out_str += " " + str(i)
            break
        x /= 10
print out_str