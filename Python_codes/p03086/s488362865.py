s = input()
ans = 0
start = 0
end = 1

def acgt(s):
    count = 0
    for i in ["A","T","G","C"]:
        count += s.count(i)
    return count

while start < len(s):
    check = s[start:end]
    while len(check) == acgt(check) and end <= len(s):
        end += 1
        check = s[start:end]
    lenth = end - start -1
    ans = max(ans, lenth)
    start = end
print(ans)