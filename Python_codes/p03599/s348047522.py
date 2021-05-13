#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C, D, E, F = map(int, input().split())

    A *= 100
    B *= 100

    water = []
    sugar = []

    for i in range(1 + F // A):
        for j in range(1 + F // B):
            if i * A + j * B <= F:
                water.append(i * A + j * B)

    for i in range(1 + F // C):
        for j in range(1 + F // D):
            if i * C + j * D <= F:
                sugar.append(i * C + j * D)

    max_sugar_percent = 0
    max_water = 0
    max_sugar = 0

    water.sort()
    sugar.sort()

    for w in water:
        for s in sugar:
            if w + s > F:
                break

            if s > E * w / 100:
                break

            sugar_percent = w and(100 * s) / (w + s)
            if sugar_percent >= max_sugar_percent:
                max_sugar_percent = sugar_percent
                max_sugar = s
                max_water = w + s

    print(max_water, max_sugar)


if __name__ == "__main__":
    main()
