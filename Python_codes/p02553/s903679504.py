def main():
    a, b, c, d = map(int, input().split())
    if a >= 0:
        if b >= 0:
            if c >= 0:
                return b * d
            
            if d >= 0:
                return max(a*c, b*d)
            return a * d
    else:
        if b >= 0:
            if c >= 0:
                return b * d
            if d >= 0:
                return max(a*c, b*d)
            return a * c
        if c >= 0:
            return b * c
        if d >= 0:
            return a * c
        return a * c

if __name__ == "__main__":
    print(main())