string = input()
cnt = int(input())

for i in range(cnt):
    linearr = (input().split())
    cmd = linearr[0]
    a = int(linearr[1])
    b = int(linearr[2])

    if cmd == "print":
        print(string[a:b+1])
    elif cmd == "replace":
        string = string[:a] + linearr[3] + string[b + 1:]
    elif cmd == "reverse":
        string = string[:a] + string[a:b + 1][::-1] + string[b + 1:]