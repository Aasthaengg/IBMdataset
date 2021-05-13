s = list(input())
sorted_s = sorted(s)

print("Yes") if sorted_s[0] == sorted_s[1] and sorted_s[2] == sorted_s[3] and sorted_s[1] != sorted_s[2] else print("No") 