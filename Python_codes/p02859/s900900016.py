import sys

def propare():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = int(next(tokens))

    solve(r)

def solve(r: int):
    print(int(r*r/1))
    return


 
if __name__ == "__main__":
    propare()