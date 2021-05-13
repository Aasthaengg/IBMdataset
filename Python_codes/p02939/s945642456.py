from collections import deque
def main4():
    S = input()

    i = 0
    tmp = ""
    sub = deque()
    while True:
        j = 1
        while i + j <= len(S):
            if S[i:i+j] != tmp:
                sub.append(S[i:i+j])
                tmp = S[i:i+j]
                i = i + j
                break
            else:
                j += 1

        if i + j > len(S):
            if S[i:i+j] != "":
                if sub[-1] == S[i:i+j]:
                    e = sub.pop()
                    sub.append(e + S[i:i+j])
                else:
                    sub.append(S[i:i+j])
            break
    
    print(len(sub))
    
if __name__ == "__main__":
    main4()