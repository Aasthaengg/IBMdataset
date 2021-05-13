n = int(input())
answer = [0 for i in range(4)]
for i in range(n):
    s = input()
    if s == "AC":
        answer[0] += 1
    elif s == "WA":
        answer[1] += 1
    elif s == "TLE":
        answer[2] += 1
    else:
        answer[3] += 1

print("AC x", answer[0])
print("WA x", answer[1])
print("TLE x", answer[2])
print("RE x", answer[3])
