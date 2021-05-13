def main():
    S = list(input())
    ans = 1000
    for t in [chr(ord('a')+i) for i in range(26)]:
        if S.count(t) == len(S):
            print(0)
            return
        nextS = S[:]
        count = 0
        while True:
            changed = False
            deleted = False
            nextnextS = []
            num = 0
            for i in range(len(nextS)-1):
                if nextS[i] == t or nextS[i+1] == t:
                    nextnextS.append(t)
                else:
                    # if num == 0:
                    #     deleted = True
                    #     num += 1
                    # else:
                        changed = True
                        nextnextS.append(nextS[i])
            nextS = nextnextS
            
            count += 1
            if not changed:
                if deleted:
                    count += 1
                break

            
            # print(t,nextS,count)
        ans = min(ans,count)
    print(ans)

        


main()