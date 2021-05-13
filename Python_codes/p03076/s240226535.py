from itertools import permutations
def main():
    a=[int(input()) for _ in range(5)]
    ans=[]
    for x in permutations(a):
        t = 0
        for y in x:
            if t % 10 != 0:
                t = (t//10 + 1) * 10
            t += y
        ans.append(t)
    print(min(ans))
            
    
if __name__ == "__main__":
    main()