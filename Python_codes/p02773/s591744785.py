N = int(input())

dict = {}
for i in range(N):
    s = input()
    if(s in dict):
        dict[s] += 1
    else:
        dict[s] = 1

max = max(dict.values())
for key, val in sorted(dict.items()):
    if(val == max):
        print(key)
