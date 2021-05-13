from collections import Counter 
def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(int(input()))
    d = Counter(d)
    print(len(d))
    
main()
