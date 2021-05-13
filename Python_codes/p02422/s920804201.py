string = input()
raw = int(input())
for _ in range(raw):
    hoge = input().strip().split()
    if hoge[0] == 'print':
        print (string[int(hoge[1]):int(hoge[2])+1])
    elif hoge[0] == 'reverse':
        string = string[:int(hoge[1])] + string[int(hoge[1]):int(hoge[2])+1][::-1] + string[int(hoge[2])+1:]
    elif hoge[0] == 'replace':
        string = string[:int(hoge[1])] + hoge[3] + string[int(hoge[2])+1:]
