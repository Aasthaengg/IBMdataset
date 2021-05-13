import re

def main():
    N = str(input())
    if re.match("^.*keyence$", N) or re.match("^k.*eyence$", N) or re.match("^ke.*yence$", N) or re.match("^key.*ence$", N) or re.match("^keye.*nce$", N) or re.match("^keyen.*ce$", N) or re.match("^keyenc.*e$", N) or re.match("^keyence.*$", N):
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    main()