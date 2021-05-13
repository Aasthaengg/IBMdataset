N = int(input())
S = input()
for i in range(len(S)):
    a = ord(S[i])+N
    if a > ord('Z'):
        a -= 26
    print(chr(a),end ='')
