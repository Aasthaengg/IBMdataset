text = input()
n = int(input())

for i in range(n):
    ins = input().split()
    if ins[0] == "print":
        a, b = int(ins[1]), int(ins[2])
        print(text[a:b + 1])
    elif ins[0] == "reverse":
        a, b = int(ins[1]), int(ins[2])
        text = text[:a] + text[a:b + 1][::-1] + text[b + 1:]
    elif ins[0] == "replace":
        a, b, p = int(ins[1]), int(ins[2]), ins[3]
        text = text[:a] + p + text[b + 1:]