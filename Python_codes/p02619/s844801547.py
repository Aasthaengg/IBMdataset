def func(s,x):
    last=[0]*26
    score=0
    for i,v in enumerate(x,1):
        last[v]=i
        c=0
        for j in range(26):
            c+=s[j]*(i-last[j])
        score=score+s[i*26+v]-c
        print(score)
    return score
def main():
    d,*s=map(int,open(0).read().split())
    func(s,[t-1for t in s[-d:]])
main()