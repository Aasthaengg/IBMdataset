sen = input()
target = input()

def cilcle(s, n):
    result = ""
    for i in range(n):
        result += sen[i%len(sen)]
    return result

if target in cilcle(sen, len(sen)**2):
    print("Yes")
else:
    print("No")
