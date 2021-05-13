def main(heads, foots):
    """
    - foots != odd
    - 2*heads <= foots <= 4*heads
    """
    if foots%2 == 1:
        return 'No'
    else:
        if 2*heads <= foots <= 4*heads:
            return 'Yes' 
        else:
            return 'No'

if __name__ == '__main__':
    heads, foots = map(int, input().split())
    ans = main(heads, foots)
    print(ans)

