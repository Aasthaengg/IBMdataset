n = list(input())
s = [int(i) for i in n]

print(['No','Yes'][len(set(s[:3]))==1 or len(set(s[1:4]))==1 or len(set(s[1:4])) == 1])