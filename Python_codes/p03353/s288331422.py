from sys import stdin
def main():
    #入力
    readline=stdin.readline
    s=readline().strip()
    K=int(readline())

    N=len(s)
    words=[]
    for i in range(N):
        words.append(s[i])
    for i in range(N-1):
        words.append(s[i:i+2])
    for i in range(N-2):
        words.append(s[i:i+3])
    for i in range(N-3):
        words.append(s[i:i+4])
    for i in range(N-4):
        words.append(s[i:i+5])
    words=set(words)
    words=list(words)
    words.sort()
    print(words[K-1])
    
if __name__=="__main__":
    main()