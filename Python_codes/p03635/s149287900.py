def main():
    n, m = map(int, input().split())
    all_place = ((n+1)*(m+1))
    outside = (2*(n+1))+(2*(m+1))-4
    print(all_place-outside)
main()