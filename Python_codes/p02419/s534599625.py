import sys
W = input().lower()
cnt = 0
for line in sys.stdin:
    s = line.lower()
    T = s.split(" ")
    for i in range(len(T)):
        if T[i] == "end_of_text":
            break
        if T[i].strip("\".,\n") == W:
            cnt += 1
print(cnt)