s = input()

min_v = 9999
for i in range(len(s) - 2):
    # print(s[i:i + 3])
    n = int(s[i:i + 3])
    min_v = min(min_v, abs(753 - n))
    
print(min_v)