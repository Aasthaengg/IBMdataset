n = int(input())
string = input()

left = string[:0]
right = string[0:]
w, r = left.count("W"), right.count("R")
count = max(w,r)

for i in range(1,n+1):
    next_str = string[i-1]
    if next_str == "W":
        w +=1
    else:
        r -= 1
    tmp = max(w,r)
    if tmp < count:
        count = tmp
        
print(count)