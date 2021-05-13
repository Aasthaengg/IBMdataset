def resolve():
    S = list(input())
    mindiff = float("inf")
    for i in range(len(S)-2):
        val = int(S[i]+S[i+1]+S[i+2])
        mindiff = min(mindiff, abs(753-val))
    print(mindiff)

if '__main__' == __name__:
    resolve()