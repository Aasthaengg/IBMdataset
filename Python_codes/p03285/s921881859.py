import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        n=int(input())
        for cake in range(26):
            for donut in range(15):
                if cake*4+donut*7==n:
                    return 'Yes'
        return 'No'
    print(main())
resolve()