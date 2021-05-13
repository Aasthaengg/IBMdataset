#coding: utf-8
#!/home/nicetacks/.pyenv/shims/python3

s = input()

while "BC" in s:
    s = s.replace("BC", "D")

ret  = 0
numA = 0
for i in range(len(s)):
    if s[i] == "A":
        numA += 1
    elif s[i] == "D":
        ret += numA
    else:
        numA = 0

print(ret)

