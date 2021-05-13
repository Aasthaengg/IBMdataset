
url = "https://atcoder.jp//contests/abc051/tasks/abc051_c"
def search_route(f, t):
    route = ''
    y = t[1] - f[1]
    tmp_y = 'U'*y if y >= 0 else 'D'*(y*-1)
    x = t[0] - f[0]
    tmp_x = 'R'*x if x >= 0 else 'L'*(x*-1)
    route = tmp_y + tmp_x
    return route


def main():
    t = list(map(int, input().split()))
    route = search_route(t[:2], t[2:]) + search_route(t[2:], t[:2])
    tmp = t[:]
    t[0] -= 1
    t[3] += 1
    route_2 = 'L' + search_route(t[:2], t[2:]) + 'D'
    t = tmp
    t[1] -= 1
    t[2] += 1
    route_2 = route_2 + 'R' + search_route(t[2:], t[:2]) + 'U'

    print(route+route_2)


if __name__ == '__main__':
    main()

